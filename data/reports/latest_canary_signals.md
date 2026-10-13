# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T22:52:34.807412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `0.1425` n `235`; crypto_major avg `0.1047` n `8`; equity avg `0.0695` n `151`; fx avg `-0.0106` n `6`; index avg `0.0291` n `26`; metal avg `0.0122` n `20`; unknown avg `0.2838` n `1135`
- 1h: commodity avg `0.039` n `13`; crypto_alt avg `-0.1845` n `235`; crypto_major avg `-0.0229` n `8`; equity avg `0.1277` n `151`; fx avg `0.0011` n `6`; index avg `0.0276` n `26`; metal avg `-0.0127` n `20`; unknown avg `0.3042` n `1077`
- 4h: commodity avg `0.1268` n `13`; crypto_alt avg `0.2625` n `235`; crypto_major avg `0.0372` n `8`; equity avg `0.5524` n `151`; fx avg `-0.0285` n `6`; index avg `0.0571` n `26`; metal avg `-0.0218` n `20`; unknown avg `0.6785` n `1019`
- 24h: commodity avg `0.7637` n `13`; crypto_alt avg `-0.0201` n `235`; crypto_major avg `0.4947` n `8`; equity avg `-0.3241` n `151`; fx avg `0.155` n `6`; index avg `-0.1148` n `26`; metal avg `-0.2774` n `20`; unknown avg `-0.142` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `667`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1426`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1233`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0912`, n `667`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0851`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0808`, n `667`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0807`, n `669`, weak_sample_signal
