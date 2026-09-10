# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T05:07:27.075247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.1304` n `233`; crypto_major avg `-0.1158` n `8`; equity avg `-0.0274` n `134`; fx avg `0.0009` n `6`; index avg `-0.0014` n `26`; metal avg `0.0181` n `20`; unknown avg `2.0109` n `795`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.3648` n `233`; crypto_major avg `-0.2542` n `8`; equity avg `0.0797` n `134`; fx avg `0.0061` n `6`; index avg `0.0292` n `26`; metal avg `-0.0014` n `20`; unknown avg `0.7929` n `789`
- 4h: commodity avg `-0.0845` n `12`; crypto_alt avg `-0.3861` n `233`; crypto_major avg `-0.1143` n `8`; equity avg `0.1627` n `134`; fx avg `-0.003` n `6`; index avg `0.1055` n `26`; metal avg `-0.0071` n `20`; unknown avg `1.3309` n `789`
- 24h: commodity avg `0.0476` n `12`; crypto_alt avg `-3.7564` n `233`; crypto_major avg `-2.4959` n `8`; equity avg `-1.0918` n `134`; fx avg `0.0356` n `6`; index avg `-0.1502` n `26`; metal avg `0.3954` n `20`; unknown avg `1.3411` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
