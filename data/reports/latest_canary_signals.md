# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T22:07:25.775807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `-0.3879` n `231`; crypto_major avg `-0.2714` n `8`; equity avg `-0.0994` n `122`; fx avg `0.0058` n `6`; index avg `-0.0438` n `25`; metal avg `-0.0387` n `20`; unknown avg `0.128` n `793`
- 1h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.2157` n `231`; crypto_major avg `0.0577` n `8`; equity avg `-0.0828` n `122`; fx avg `-0.0134` n `6`; index avg `-0.0406` n `25`; metal avg `-0.0517` n `20`; unknown avg `0.2095` n `793`
- 4h: commodity avg `-0.0823` n `12`; crypto_alt avg `0.5751` n `231`; crypto_major avg `0.8667` n `8`; equity avg `0.0701` n `122`; fx avg `-0.0928` n `6`; index avg `-0.0132` n `25`; metal avg `-0.0006` n `20`; unknown avg `1.9115` n `793`
- 24h: commodity avg `-0.1698` n `12`; crypto_alt avg `4.1827` n `231`; crypto_major avg `1.8815` n `8`; equity avg `0.6719` n `122`; fx avg `-0.0918` n `6`; index avg `0.0787` n `25`; metal avg `0.0719` n `20`; unknown avg `6.4143` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
