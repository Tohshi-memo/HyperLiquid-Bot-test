# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T20:22:26.761210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0397` n `230`; crypto_major avg `-0.0186` n `8`; equity avg `0.0051` n `114`; fx avg `0.0031` n `6`; index avg `-0.001` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0215` n `792`
- 1h: commodity avg `0.0539` n `12`; crypto_alt avg `-0.1878` n `230`; crypto_major avg `-0.0916` n `8`; equity avg `-0.0137` n `114`; fx avg `0.0026` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.0943` n `792`
- 4h: commodity avg `0.4504` n `12`; crypto_alt avg `-0.296` n `230`; crypto_major avg `-0.2955` n `8`; equity avg `-0.6107` n `114`; fx avg `0.0088` n `6`; index avg `-0.1491` n `25`; metal avg `-0.1148` n `20`; unknown avg `0.1503` n `792`
- 24h: commodity avg `0.3941` n `12`; crypto_alt avg `-0.2841` n `230`; crypto_major avg `0.6672` n `8`; equity avg `0.9946` n `114`; fx avg `0.0141` n `6`; index avg `0.0557` n `25`; metal avg `0.2157` n `20`; unknown avg `0.2264` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
