# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T12:07:25.633961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0371` n `12`; crypto_alt avg `-0.0617` n `230`; crypto_major avg `-0.1578` n `8`; equity avg `-0.2557` n `96`; fx avg `-0.0031` n `6`; index avg `-0.0308` n `25`; metal avg `-0.0721` n `20`; unknown avg `0.0313` n `769`
- 1h: commodity avg `0.067` n `12`; crypto_alt avg `-0.0593` n `230`; crypto_major avg `-0.0364` n `8`; equity avg `-0.4805` n `96`; fx avg `0.0027` n `6`; index avg `-0.0815` n `25`; metal avg `-0.0619` n `20`; unknown avg `0.2771` n `769`
- 4h: commodity avg `0.3333` n `12`; crypto_alt avg `0.3128` n `230`; crypto_major avg `0.3707` n `8`; equity avg `0.3012` n `96`; fx avg `-0.012` n `6`; index avg `0.0095` n `25`; metal avg `-0.135` n `20`; unknown avg `0.1337` n `768`
- 24h: commodity avg `-0.0246` n `12`; crypto_alt avg `-1.4383` n `230`; crypto_major avg `-2.5449` n `8`; equity avg `-4.392` n `94`; fx avg `-0.0577` n `6`; index avg `-0.5689` n `25`; metal avg `-0.8133` n `20`; unknown avg `-0.4181` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
