# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T23:37:33.109389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `0.0106` n `237`; crypto_major avg `-0.0469` n `8`; equity avg `0.0309` n `151`; fx avg `-0.0037` n `6`; index avg `0.0209` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.0386` n `1199`
- 1h: commodity avg `0.0243` n `13`; crypto_alt avg `-0.2932` n `237`; crypto_major avg `-0.3699` n `8`; equity avg `-0.2312` n `151`; fx avg `-0.0129` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0635` n `20`; unknown avg `0.2695` n `1165`
- 4h: commodity avg `0.0081` n `13`; crypto_alt avg `0.5124` n `237`; crypto_major avg `0.4852` n `8`; equity avg `1.3163` n `151`; fx avg `-0.0192` n `6`; index avg `0.1842` n `26`; metal avg `0.0107` n `20`; unknown avg `0.3329` n `1035`
- 24h: commodity avg `0.0077` n `13`; crypto_alt avg `2.0781` n `237`; crypto_major avg `1.3137` n `8`; equity avg `1.2226` n `151`; fx avg `0.0054` n `6`; index avg `0.1218` n `26`; metal avg `0.0533` n `20`; unknown avg `211.4659` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
