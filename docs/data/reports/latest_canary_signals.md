# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T07:37:33.337508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0665` n `12`; crypto_alt avg `-0.138` n `230`; crypto_major avg `-0.1303` n `8`; equity avg `-0.0458` n `100`; fx avg `-0.0071` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0358` n `20`; unknown avg `0.0598` n `775`
- 1h: commodity avg `0.0274` n `12`; crypto_alt avg `-0.1981` n `230`; crypto_major avg `-0.3156` n `8`; equity avg `0.0754` n `100`; fx avg `-0.0498` n `6`; index avg `-0.0059` n `25`; metal avg `0.1046` n `20`; unknown avg `0.0891` n `775`
- 4h: commodity avg `-0.3282` n `12`; crypto_alt avg `0.0061` n `230`; crypto_major avg `0.3192` n `8`; equity avg `0.6553` n `100`; fx avg `-0.0053` n `6`; index avg `0.1227` n `25`; metal avg `0.2244` n `20`; unknown avg `0.0312` n `759`
- 24h: commodity avg `-0.757` n `12`; crypto_alt avg `0.7635` n `230`; crypto_major avg `1.3924` n `8`; equity avg `1.3774` n `100`; fx avg `0.0742` n `6`; index avg `0.177` n `25`; metal avg `0.5301` n `20`; unknown avg `-0.013` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
