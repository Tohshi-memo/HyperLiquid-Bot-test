# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T12:07:31.017806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1243` n `12`; crypto_alt avg `0.1218` n `230`; crypto_major avg `0.1561` n `8`; equity avg `0.1296` n `100`; fx avg `0.0031` n `6`; index avg `0.0226` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0462` n `776`
- 1h: commodity avg `0.0865` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `-0.0531` n `8`; equity avg `-0.1139` n `100`; fx avg `0.0033` n `6`; index avg `-0.0267` n `25`; metal avg `-0.0333` n `20`; unknown avg `0.053` n `776`
- 4h: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.1288` n `230`; crypto_major avg `0.0231` n `8`; equity avg `-0.1089` n `100`; fx avg `-0.024` n `6`; index avg `0.0015` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.0842` n `775`
- 24h: commodity avg `-0.4878` n `12`; crypto_alt avg `0.4873` n `230`; crypto_major avg `1.1319` n `8`; equity avg `1.0234` n `100`; fx avg `0.0885` n `6`; index avg `0.1187` n `25`; metal avg `0.3109` n `20`; unknown avg `-0.1006` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
