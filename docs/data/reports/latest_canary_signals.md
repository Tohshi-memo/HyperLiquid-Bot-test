# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T07:07:32.032715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `-0.0743` n `239`; crypto_major avg `0.0885` n `8`; equity avg `0.1945` n `158`; fx avg `0.0105` n `6`; index avg `0.0417` n `27`; metal avg `0.0036` n `20`; unknown avg `0.03` n `1259`
- 1h: commodity avg `-0.063` n `13`; crypto_alt avg `0.4533` n `239`; crypto_major avg `0.3842` n `8`; equity avg `0.7337` n `158`; fx avg `-0.0176` n `6`; index avg `0.082` n `27`; metal avg `0.0793` n `20`; unknown avg `0.0538` n `1251`
- 4h: commodity avg `-0.0393` n `13`; crypto_alt avg `-0.2171` n `239`; crypto_major avg `-0.0138` n `8`; equity avg `-0.2775` n `158`; fx avg `-0.0164` n `6`; index avg `-0.1102` n `27`; metal avg `-0.1215` n `20`; unknown avg `-0.2496` n `1209`
- 24h: commodity avg `-2.0321` n `13`; crypto_alt avg `1.308` n `239`; crypto_major avg `2.5284` n `8`; equity avg `-1.9069` n `158`; fx avg `0.0637` n `6`; index avg `-0.0556` n `27`; metal avg `0.8936` n `20`; unknown avg `30.785` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2506`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
