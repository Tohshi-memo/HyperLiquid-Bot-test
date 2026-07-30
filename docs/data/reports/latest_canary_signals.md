# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T17:07:24.512683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.1172` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1776` n `230`; crypto_major avg `-0.044` n `8`; equity avg `0.1491` n `102`; fx avg `0.0086` n `6`; index avg `0.0588` n `25`; metal avg `0.0204` n `20`; unknown avg `-0.0438` n `779`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.2806` n `230`; crypto_major avg `-0.0715` n `8`; equity avg `-0.0538` n `102`; fx avg `0.0537` n `6`; index avg `0.0032` n `25`; metal avg `-0.0155` n `20`; unknown avg `-0.0523` n `779`
- 4h: commodity avg `0.3309` n `12`; crypto_alt avg `-0.1023` n `230`; crypto_major avg `0.6515` n `8`; equity avg `2.7687` n `102`; fx avg `-0.2261` n `6`; index avg `0.2852` n `25`; metal avg `0.3242` n `20`; unknown avg `0.0919` n `779`
- 24h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.5806` n `230`; crypto_major avg `1.3835` n `8`; equity avg `4.4154` n `102`; fx avg `-0.2774` n `6`; index avg `0.476` n `25`; metal avg `0.6988` n `20`; unknown avg `-0.0629` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
