# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T09:22:26.807242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0988` n `12`; crypto_alt avg `0.0816` n `230`; crypto_major avg `0.0339` n `8`; equity avg `0.0865` n `98`; fx avg `-0.0037` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0185` n `773`
- 1h: commodity avg `0.1198` n `12`; crypto_alt avg `0.124` n `230`; crypto_major avg `0.0554` n `8`; equity avg `0.2606` n `98`; fx avg `-0.031` n `6`; index avg `0.0279` n `25`; metal avg `0.0124` n `20`; unknown avg `0.0291` n `773`
- 4h: commodity avg `0.383` n `12`; crypto_alt avg `0.0515` n `230`; crypto_major avg `-0.1455` n `8`; equity avg `-0.1847` n `98`; fx avg `-0.0499` n `6`; index avg `-0.0837` n `25`; metal avg `-0.075` n `20`; unknown avg `-0.0231` n `739`
- 24h: commodity avg `0.9057` n `12`; crypto_alt avg `-0.5929` n `230`; crypto_major avg `-1.3529` n `8`; equity avg `0.4708` n `98`; fx avg `-0.0216` n `6`; index avg `-0.0196` n `25`; metal avg `0.2814` n `20`; unknown avg `0.1111` n `739`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1072`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0786`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0711`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0682`, n `666`, weak_sample_signal
