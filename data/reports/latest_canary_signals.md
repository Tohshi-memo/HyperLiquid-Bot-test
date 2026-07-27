# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T00:52:28.506615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `0.0653` n `230`; crypto_major avg `0.0945` n `8`; equity avg `0.1896` n `100`; fx avg `0.0208` n `6`; index avg `0.0507` n `25`; metal avg `0.0267` n `20`; unknown avg `-0.1591` n `775`
- 1h: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.1578` n `230`; crypto_major avg `-0.3265` n `8`; equity avg `-0.2746` n `100`; fx avg `0.0891` n `6`; index avg `-0.0976` n `25`; metal avg `0.051` n `20`; unknown avg `-0.086` n `775`
- 4h: commodity avg `-0.3815` n `12`; crypto_alt avg `0.8936` n `230`; crypto_major avg `0.8316` n `8`; equity avg `0.4675` n `100`; fx avg `0.0614` n `6`; index avg `0.1151` n `25`; metal avg `0.2835` n `20`; unknown avg `-0.007` n `775`
- 24h: commodity avg `-0.5158` n `12`; crypto_alt avg `1.5926` n `230`; crypto_major avg `1.5904` n `8`; equity avg `1.0028` n `100`; fx avg `0.119` n `6`; index avg `0.1997` n `25`; metal avg `0.4762` n `20`; unknown avg `0.0579` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
