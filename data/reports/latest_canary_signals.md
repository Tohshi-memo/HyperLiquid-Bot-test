# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T09:18:46.132225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `0.0075` n `230`; crypto_major avg `0.017` n `8`; equity avg `0.0721` n `96`; fx avg `0.0173` n `6`; index avg `0.0077` n `25`; metal avg `0.0222` n `20`; unknown avg `-0.0035` n `768`
- 1h: commodity avg `0.147` n `12`; crypto_alt avg `0.294` n `230`; crypto_major avg `0.2427` n `8`; equity avg `0.2575` n `96`; fx avg `0.0254` n `6`; index avg `0.027` n `25`; metal avg `0.1095` n `20`; unknown avg `-0.0561` n `768`
- 4h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.5178` n `230`; crypto_major avg `-0.4058` n `8`; equity avg `-0.5187` n `96`; fx avg `0.054` n `6`; index avg `-0.078` n `25`; metal avg `0.0954` n `20`; unknown avg `-0.071` n `736`
- 24h: commodity avg `0.0691` n `12`; crypto_alt avg `-1.5524` n `230`; crypto_major avg `-2.7882` n `8`; equity avg `-5.7497` n `94`; fx avg `-0.0178` n `6`; index avg `-0.8226` n `25`; metal avg `-0.7565` n `20`; unknown avg `-0.5129` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
