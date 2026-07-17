# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T04:22:24.853322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `-0.2131` n `230`; crypto_major avg `-0.2333` n `8`; equity avg `-0.0903` n `96`; fx avg `-0.0026` n `6`; index avg `-0.0272` n `25`; metal avg `0.0005` n `20`; unknown avg `0.0072` n `768`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `-0.4815` n `230`; crypto_major avg `-0.5455` n `8`; equity avg `-0.519` n `95`; fx avg `-0.0022` n `6`; index avg `-0.1302` n `25`; metal avg `-0.1299` n `20`; unknown avg `0.0639` n `768`
- 4h: commodity avg `-0.014` n `12`; crypto_alt avg `-0.3327` n `230`; crypto_major avg `-0.6496` n `8`; equity avg `-1.2055` n `94`; fx avg `-0.0219` n `6`; index avg `-0.2047` n `25`; metal avg `-0.1354` n `20`; unknown avg `0.0164` n `768`
- 24h: commodity avg `-0.0761` n `12`; crypto_alt avg `-2.0309` n `230`; crypto_major avg `-3.0927` n `8`; equity avg `-5.399` n `94`; fx avg `-0.1389` n `6`; index avg `-0.7348` n `25`; metal avg `-0.8328` n `20`; unknown avg `-0.4674` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
