# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T06:07:28.055529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `-0.168` n `230`; crypto_major avg `-0.1577` n `8`; equity avg `-0.2342` n `98`; fx avg `-0.0128` n `6`; index avg `-0.0543` n `25`; metal avg `-0.0268` n `20`; unknown avg `-0.0629` n `740`
- 1h: commodity avg `-0.0164` n `12`; crypto_alt avg `-0.5225` n `230`; crypto_major avg `-0.8205` n `8`; equity avg `-0.6661` n `98`; fx avg `-0.0293` n `6`; index avg `-0.1059` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.1809` n `739`
- 4h: commodity avg `-0.1058` n `12`; crypto_alt avg `-0.807` n `230`; crypto_major avg `-1.1206` n `8`; equity avg `-1.4698` n `98`; fx avg `0.0044` n `6`; index avg `-0.2613` n `25`; metal avg `-0.0409` n `20`; unknown avg `-0.2577` n `739`
- 24h: commodity avg `0.5543` n `12`; crypto_alt avg `-0.9634` n `230`; crypto_major avg `-1.2631` n `8`; equity avg `0.9076` n `98`; fx avg `0.0593` n `6`; index avg `0.0649` n `25`; metal avg `0.608` n `20`; unknown avg `0.0679` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0973`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0713`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `666`, weak_sample_signal
