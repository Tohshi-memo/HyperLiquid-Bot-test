# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T22:52:27.736502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1517` n `12`; crypto_alt avg `-0.1049` n `230`; crypto_major avg `-0.0796` n `8`; equity avg `0.0219` n `102`; fx avg `-0.0105` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.0099` n `783`
- 1h: commodity avg `0.1876` n `12`; crypto_alt avg `-0.3854` n `230`; crypto_major avg `-0.261` n `8`; equity avg `-0.0788` n `102`; fx avg `-0.0402` n `6`; index avg `-0.0493` n `25`; metal avg `-0.1925` n `20`; unknown avg `0.069` n `783`
- 4h: commodity avg `0.0536` n `12`; crypto_alt avg `-0.1418` n `230`; crypto_major avg `0.0603` n `8`; equity avg `0.2237` n `102`; fx avg `0.094` n `6`; index avg `0.0062` n `25`; metal avg `-0.0728` n `20`; unknown avg `1.1375` n `782`
- 24h: commodity avg `-1.1057` n `12`; crypto_alt avg `1.1298` n `230`; crypto_major avg `1.6755` n `8`; equity avg `1.547` n `102`; fx avg `-0.036` n `6`; index avg `0.3085` n `25`; metal avg `0.2018` n `20`; unknown avg `1.6187` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
