# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T11:22:17.131077+00:00`
- Correlation status: `ready`
- Asset price records: `545`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2543` n `12`; crypto_alt avg `0.0214` n `228`; crypto_major avg `0.0363` n `8`; equity avg `-0.1974` n `65`; fx avg `-0.0084` n `4`; index avg `-0.0312` n `23`; metal avg `-0.0861` n `18`; unknown avg `0.0409` n `366`
- 1h: commodity avg `-0.3769` n `12`; crypto_alt avg `0.2573` n `228`; crypto_major avg `0.0745` n `8`; equity avg `-0.1288` n `65`; fx avg `-0.0174` n `4`; index avg `-0.0018` n `23`; metal avg `-0.07` n `18`; unknown avg `0.2278` n `366`
- 4h: commodity avg `-0.0287` n `12`; crypto_alt avg `0.0781` n `228`; crypto_major avg `-0.2982` n `8`; equity avg `-0.2256` n `65`; fx avg `0.1129` n `4`; index avg `-0.1468` n `23`; metal avg `0.1404` n `18`; unknown avg `0.0603` n `358`
- 24h: commodity avg `0.2725` n `7`; crypto_alt avg `-0.0999` n `223`; crypto_major avg `-2.5889` n `7`; equity avg `-0.2108` n `47`; fx avg `0.1955` n `4`; index avg `0.0333` n `6`; metal avg `0.8518` n `7`; unknown avg `0.9124` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1306`, n `541`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `541`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0906`, n `541`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.083`, n `537`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0792`, n `537`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `537`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `541`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0733`, n `537`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `537`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0684`, n `537`, weak_sample_signal
