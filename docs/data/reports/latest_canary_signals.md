# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T13:07:31.943452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `13`; crypto_alt avg `-0.1891` n `237`; crypto_major avg `-0.1789` n `8`; equity avg `0.0665` n `151`; fx avg `-0.0019` n `6`; index avg `0.0158` n `26`; metal avg `-0.0171` n `20`; unknown avg `0.8067` n `1196`
- 1h: commodity avg `-0.1837` n `13`; crypto_alt avg `0.2435` n `237`; crypto_major avg `0.2027` n `8`; equity avg `0.4375` n `151`; fx avg `0.0197` n `6`; index avg `0.0834` n `26`; metal avg `0.0109` n `20`; unknown avg `2.0568` n `1196`
- 4h: commodity avg `-0.1902` n `13`; crypto_alt avg `0.4137` n `237`; crypto_major avg `0.3453` n `8`; equity avg `0.0307` n `151`; fx avg `0.037` n `6`; index avg `0.0587` n `26`; metal avg `-0.0512` n `20`; unknown avg `5.0497` n `1188`
- 24h: commodity avg `0.1777` n `13`; crypto_alt avg `-0.2181` n `237`; crypto_major avg `-0.8626` n `8`; equity avg `-2.3027` n `151`; fx avg `-0.0115` n `6`; index avg `-0.2785` n `26`; metal avg `-0.2531` n `20`; unknown avg `4.5845` n `1069`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
