# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T19:07:26.074088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `12`; crypto_alt avg `0.0005` n `232`; crypto_major avg `0.0943` n `8`; equity avg `0.1149` n `133`; fx avg `0.0055` n `6`; index avg `0.0073` n `26`; metal avg `-0.0032` n `20`; unknown avg `-0.3076` n `790`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `0.1397` n `232`; crypto_major avg `0.1346` n `8`; equity avg `0.2872` n `133`; fx avg `0.0144` n `6`; index avg `0.0023` n `26`; metal avg `0.0` n `20`; unknown avg `-0.3523` n `790`
- 4h: commodity avg `0.0746` n `12`; crypto_alt avg `0.5187` n `232`; crypto_major avg `0.5185` n `8`; equity avg `0.8589` n `133`; fx avg `-0.0024` n `6`; index avg `0.05` n `26`; metal avg `-0.0151` n `20`; unknown avg `-0.4425` n `789`
- 24h: commodity avg `0.2209` n `12`; crypto_alt avg `-0.0449` n `232`; crypto_major avg `-0.1649` n `8`; equity avg `0.8204` n `133`; fx avg `-0.3387` n `6`; index avg `0.1278` n `26`; metal avg `0.4291` n `20`; unknown avg `-0.2146` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
