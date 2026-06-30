# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T09:22:29.086306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0278` n `12`; crypto_alt avg `-0.0637` n `228`; crypto_major avg `-0.0712` n `8`; equity avg `-0.0278` n `88`; fx avg `0.0019` n `6`; index avg `0.0048` n `23`; metal avg `0.0081` n `20`; unknown avg `0.0108` n `765`
- 1h: commodity avg `0.0503` n `12`; crypto_alt avg `-0.2522` n `228`; crypto_major avg `-0.1919` n `8`; equity avg `-0.1397` n `88`; fx avg `-0.0287` n `6`; index avg `-0.0323` n `23`; metal avg `-0.037` n `20`; unknown avg `-0.0767` n `765`
- 4h: commodity avg `0.2152` n `12`; crypto_alt avg `-0.532` n `228`; crypto_major avg `-0.3672` n `8`; equity avg `-0.4632` n `88`; fx avg `0.0563` n `6`; index avg `-0.1305` n `23`; metal avg `0.4943` n `20`; unknown avg `-0.5732` n `737`
- 24h: commodity avg `0.0514` n `12`; crypto_alt avg `-0.794` n `228`; crypto_major avg `0.3149` n `8`; equity avg `1.3936` n `88`; fx avg `0.1583` n `6`; index avg `0.1282` n `23`; metal avg `-0.0467` n `20`; unknown avg `8.9487` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
