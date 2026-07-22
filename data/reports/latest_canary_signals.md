# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T15:37:34.573419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `-0.0574` n `230`; crypto_major avg `-0.1114` n `8`; equity avg `-0.0864` n `98`; fx avg `0.0013` n `6`; index avg `-0.0034` n `25`; metal avg `-0.013` n `20`; unknown avg `0.0829` n `773`
- 1h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.1967` n `230`; crypto_major avg `0.3313` n `8`; equity avg `0.2463` n `98`; fx avg `-0.0067` n `6`; index avg `0.0578` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.05` n `773`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `0.3831` n `230`; crypto_major avg `0.3958` n `8`; equity avg `1.2016` n `98`; fx avg `-0.0179` n `6`; index avg `0.2076` n `25`; metal avg `0.1612` n `20`; unknown avg `10.9376` n `773`
- 24h: commodity avg `0.452` n `12`; crypto_alt avg `-0.1308` n `230`; crypto_major avg `-0.6757` n `8`; equity avg `0.3705` n `98`; fx avg `-0.023` n `6`; index avg `-0.0438` n `25`; metal avg `0.3955` n `20`; unknown avg `1.1241` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1057`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0917`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0729`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.071`, n `666`, weak_sample_signal
