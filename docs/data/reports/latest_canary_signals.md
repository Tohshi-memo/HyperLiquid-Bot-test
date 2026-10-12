# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T01:22:27.078250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `-0.1774` n `235`; crypto_major avg `-0.0354` n `8`; equity avg `-0.0643` n `150`; fx avg `-0.0049` n `6`; index avg `-0.0286` n `26`; metal avg `0.0442` n `20`; unknown avg `-0.0785` n `1134`
- 1h: commodity avg `-0.1129` n `13`; crypto_alt avg `-0.2762` n `235`; crypto_major avg `0.1017` n `8`; equity avg `-0.2634` n `150`; fx avg `-0.0518` n `6`; index avg `-0.0873` n `26`; metal avg `0.0159` n `20`; unknown avg `0.0117` n `1124`
- 4h: commodity avg `-0.545` n `13`; crypto_alt avg `0.756` n `235`; crypto_major avg `0.7432` n `8`; equity avg `0.1019` n `150`; fx avg `-0.0693` n `6`; index avg `-0.0387` n `26`; metal avg `0.1505` n `20`; unknown avg `0.1166` n `1100`
- 24h: commodity avg `-0.3747` n `13`; crypto_alt avg `1.9042` n `235`; crypto_major avg `1.0389` n `8`; equity avg `0.3388` n `150`; fx avg `-0.0572` n `6`; index avg `-0.012` n `26`; metal avg `0.2015` n `20`; unknown avg `0.7265` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
