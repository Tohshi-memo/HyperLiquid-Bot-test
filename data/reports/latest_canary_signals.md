# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T10:52:25.017415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `-0.0383` n `230`; crypto_major avg `0.0313` n `8`; equity avg `0.0216` n `96`; fx avg `0.0007` n `6`; index avg `-0.0206` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.0048` n `769`
- 1h: commodity avg `0.0901` n `12`; crypto_alt avg `0.1502` n `230`; crypto_major avg `0.1248` n `8`; equity avg `0.0188` n `96`; fx avg `-0.0041` n `6`; index avg `0.0054` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.037` n `769`
- 4h: commodity avg `0.1362` n `12`; crypto_alt avg `-0.2645` n `230`; crypto_major avg `-0.0441` n `8`; equity avg `-0.059` n `96`; fx avg `0.0067` n `6`; index avg `0.0402` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.1347` n `769`
- 24h: commodity avg `0.7345` n `12`; crypto_alt avg `-0.6198` n `230`; crypto_major avg `0.1228` n `8`; equity avg `0.285` n `96`; fx avg `0.0452` n `6`; index avg `0.0921` n `25`; metal avg `0.2588` n `20`; unknown avg `0.1836` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
