# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T04:22:23.440237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0561` n `12`; crypto_alt avg `0.237` n `230`; crypto_major avg `0.1255` n `8`; equity avg `-0.0345` n `112`; fx avg `-0.0061` n `6`; index avg `0.0017` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.1316` n `784`
- 1h: commodity avg `0.0606` n `12`; crypto_alt avg `0.4527` n `230`; crypto_major avg `0.1218` n `8`; equity avg `-0.0152` n `112`; fx avg `-0.0056` n `6`; index avg `0.0023` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.0226` n `784`
- 4h: commodity avg `0.1164` n `12`; crypto_alt avg `0.3561` n `230`; crypto_major avg `-0.1471` n `8`; equity avg `-0.0757` n `112`; fx avg `-0.0046` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0174` n `20`; unknown avg `-0.2732` n `784`
- 24h: commodity avg `0.2781` n `12`; crypto_alt avg `1.7874` n `230`; crypto_major avg `0.5893` n `8`; equity avg `0.4657` n `112`; fx avg `-0.001` n `6`; index avg `0.0412` n `25`; metal avg `0.01` n `20`; unknown avg `-0.0187` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
