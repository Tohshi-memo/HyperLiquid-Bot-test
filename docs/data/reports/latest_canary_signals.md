# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T06:22:30.761930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.0744` n `230`; crypto_major avg `0.1371` n `8`; equity avg `0.1656` n `102`; fx avg `-0.0087` n `6`; index avg `0.0171` n `25`; metal avg `-0.0049` n `20`; unknown avg `0.0151` n `781`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.0604` n `230`; crypto_major avg `-0.0345` n `8`; equity avg `0.0684` n `102`; fx avg `-0.0078` n `6`; index avg `0.0168` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0286` n `765`
- 4h: commodity avg `-0.0392` n `12`; crypto_alt avg `-0.0141` n `230`; crypto_major avg `-0.1831` n `8`; equity avg `0.0359` n `102`; fx avg `-0.0168` n `6`; index avg `-0.0293` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.0341` n `765`
- 24h: commodity avg `0.8626` n `12`; crypto_alt avg `0.1889` n `230`; crypto_major avg `-1.7271` n `8`; equity avg `-2.8137` n `102`; fx avg `-0.062` n `6`; index avg `-0.403` n `25`; metal avg `-0.2852` n `20`; unknown avg `4.6545` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
