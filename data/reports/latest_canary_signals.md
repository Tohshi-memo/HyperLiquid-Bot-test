# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T03:22:28.051830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0396` n `12`; crypto_alt avg `-0.0063` n `231`; crypto_major avg `0.0037` n `8`; equity avg `0.0221` n `122`; fx avg `0.0027` n `6`; index avg `0.0027` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0421` n `797`
- 1h: commodity avg `-0.0687` n `12`; crypto_alt avg `0.1778` n `231`; crypto_major avg `0.1004` n `8`; equity avg `0.2835` n `122`; fx avg `0.063` n `6`; index avg `0.0774` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.3456` n `797`
- 4h: commodity avg `-0.1579` n `12`; crypto_alt avg `0.9943` n `231`; crypto_major avg `0.5569` n `8`; equity avg `-0.0243` n `122`; fx avg `0.0142` n `6`; index avg `0.0314` n `25`; metal avg `0.0898` n `20`; unknown avg `0.7796` n `795`
- 24h: commodity avg `-0.9009` n `12`; crypto_alt avg `-2.6363` n `231`; crypto_major avg `-2.7785` n `8`; equity avg `1.5747` n `122`; fx avg `0.0394` n `6`; index avg `0.2149` n `25`; metal avg `0.329` n `20`; unknown avg `0.2002` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
