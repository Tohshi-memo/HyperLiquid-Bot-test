# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T14:52:27.690163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0822` n `12`; crypto_alt avg `-0.1236` n `231`; crypto_major avg `-0.0135` n `8`; equity avg `0.0336` n `122`; fx avg `0.0003` n `6`; index avg `0.0031` n `25`; metal avg `0.0143` n `20`; unknown avg `0.0167` n `795`
- 1h: commodity avg `0.052` n `12`; crypto_alt avg `1.2192` n `231`; crypto_major avg `1.4481` n `8`; equity avg `0.0602` n `122`; fx avg `-0.0111` n `6`; index avg `-0.0781` n `25`; metal avg `0.2305` n `20`; unknown avg `0.48` n `795`
- 4h: commodity avg `-0.1211` n `12`; crypto_alt avg `-0.7251` n `231`; crypto_major avg `-0.5937` n `8`; equity avg `0.0785` n `122`; fx avg `0.0239` n `6`; index avg `-0.0907` n `25`; metal avg `0.0408` n `20`; unknown avg `-0.084` n `795`
- 24h: commodity avg `-0.728` n `12`; crypto_alt avg `-1.0905` n `231`; crypto_major avg `-0.3883` n `8`; equity avg `1.8475` n `122`; fx avg `0.0159` n `6`; index avg `0.2153` n `25`; metal avg `-0.2979` n `20`; unknown avg `-1.0347` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
