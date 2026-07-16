# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T05:37:25.852681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0838` n `230`; crypto_major avg `0.067` n `8`; equity avg `-0.2258` n `94`; fx avg `-0.007` n `6`; index avg `-0.0829` n `25`; metal avg `-0.0247` n `20`; unknown avg `0.0365` n `768`
- 1h: commodity avg `-0.0474` n `12`; crypto_alt avg `0.1547` n `230`; crypto_major avg `0.4182` n `8`; equity avg `0.1706` n `94`; fx avg `-0.0149` n `6`; index avg `0.0185` n `25`; metal avg `-0.0379` n `20`; unknown avg `0.6146` n `768`
- 4h: commodity avg `-0.1257` n `12`; crypto_alt avg `0.2152` n `230`; crypto_major avg `0.4296` n `8`; equity avg `0.3202` n `94`; fx avg `-0.0499` n `6`; index avg `0.0552` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.519` n `768`
- 24h: commodity avg `-0.0582` n `12`; crypto_alt avg `0.3787` n `230`; crypto_major avg `0.516` n `8`; equity avg `-2.0536` n `93`; fx avg `0.1042` n `6`; index avg `-0.4373` n `25`; metal avg `0.0478` n `20`; unknown avg `-0.1981` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
