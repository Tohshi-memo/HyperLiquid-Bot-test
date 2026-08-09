# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T17:52:27.518245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0348` n `230`; crypto_major avg `-0.0852` n `8`; equity avg `0.0204` n `112`; fx avg `0.0065` n `6`; index avg `0.006` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0279` n `785`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `0.0624` n `230`; crypto_major avg `-0.1236` n `8`; equity avg `0.0516` n `112`; fx avg `-0.0004` n `6`; index avg `0.0056` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.017` n `785`
- 4h: commodity avg `-0.0441` n `12`; crypto_alt avg `0.7542` n `230`; crypto_major avg `0.2591` n `8`; equity avg `0.1317` n `112`; fx avg `0.0162` n `6`; index avg `0.0187` n `25`; metal avg `0.0339` n `20`; unknown avg `-0.0697` n `785`
- 24h: commodity avg `0.0287` n `12`; crypto_alt avg `1.1449` n `230`; crypto_major avg `-0.0362` n `8`; equity avg `0.2473` n `112`; fx avg `0.0077` n `6`; index avg `0.0344` n `25`; metal avg `0.0691` n `20`; unknown avg `0.4227` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
