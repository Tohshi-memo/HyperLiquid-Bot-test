# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T04:07:34.843164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.0674` n `230`; crypto_major avg `-0.0323` n `8`; equity avg `-0.03` n `112`; fx avg `-0.0025` n `6`; index avg `0.0047` n `25`; metal avg `-0.0122` n `20`; unknown avg `-0.1091` n `785`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.0239` n `230`; crypto_major avg `-0.1136` n `8`; equity avg `0.0143` n `112`; fx avg `-0.0126` n `6`; index avg `0.006` n `25`; metal avg `0.0652` n `20`; unknown avg `-0.0577` n `785`
- 4h: commodity avg `0.0936` n `12`; crypto_alt avg `0.2861` n `230`; crypto_major avg `0.1504` n `8`; equity avg `-0.3807` n `112`; fx avg `0.0722` n `6`; index avg `0.0114` n `25`; metal avg `-0.0967` n `20`; unknown avg `-0.1527` n `785`
- 24h: commodity avg `0.4254` n `12`; crypto_alt avg `0.5899` n `230`; crypto_major avg `-0.0311` n `8`; equity avg `-0.2066` n `112`; fx avg `0.0837` n `6`; index avg `0.0246` n `25`; metal avg `-0.1708` n `20`; unknown avg `-0.3111` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
