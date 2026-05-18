# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T11:07:18.917603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1105` n `12`; crypto_alt avg `-0.1766` n `228`; crypto_major avg `-0.2057` n `8`; equity avg `-0.2335` n `66`; fx avg `0.0046` n `5`; index avg `-0.0728` n `23`; metal avg `-0.1357` n `18`; unknown avg `-0.0823` n `383`
- 1h: commodity avg `0.1423` n `12`; crypto_alt avg `-0.0698` n `228`; crypto_major avg `-0.0759` n `8`; equity avg `-0.304` n `66`; fx avg `-0.0009` n `5`; index avg `-0.0577` n `23`; metal avg `-0.1778` n `18`; unknown avg `0.0147` n `383`
- 4h: commodity avg `0.134` n `12`; crypto_alt avg `-0.5521` n `228`; crypto_major avg `-0.4614` n `8`; equity avg `0.0159` n `66`; fx avg `0.0316` n `5`; index avg `0.0127` n `23`; metal avg `-0.1695` n `18`; unknown avg `-0.3429` n `383`
- 24h: commodity avg `0.918` n `12`; crypto_alt avg `-3.3599` n `228`; crypto_major avg `-2.1267` n `8`; equity avg `-0.2592` n `65`; fx avg `0.0877` n `5`; index avg `0.0101` n `23`; metal avg `-0.125` n `18`; unknown avg `-0.6606` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
