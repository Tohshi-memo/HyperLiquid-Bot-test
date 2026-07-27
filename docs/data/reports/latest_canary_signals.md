# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T05:07:45.151980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `12`; crypto_alt avg `0.025` n `230`; crypto_major avg `0.0878` n `8`; equity avg `0.0271` n `100`; fx avg `-0.0004` n `6`; index avg `0.0095` n `25`; metal avg `0.0372` n `20`; unknown avg `0.0177` n `775`
- 1h: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.1132` n `230`; crypto_major avg `0.0179` n `8`; equity avg `0.2228` n `100`; fx avg `0.0007` n `6`; index avg `0.0692` n `25`; metal avg `0.0329` n `20`; unknown avg `1.1016` n `775`
- 4h: commodity avg `-0.0579` n `12`; crypto_alt avg `0.0179` n `230`; crypto_major avg `0.1926` n `8`; equity avg `0.3402` n `100`; fx avg `0.0182` n `6`; index avg `0.0401` n `25`; metal avg `-0.0534` n `20`; unknown avg `-0.4625` n `775`
- 24h: commodity avg `-0.4917` n `12`; crypto_alt avg `1.208` n `230`; crypto_major avg `1.3053` n `8`; equity avg `0.9435` n `100`; fx avg `0.0698` n `6`; index avg `0.1106` n `25`; metal avg `0.3454` n `20`; unknown avg `-0.0148` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
