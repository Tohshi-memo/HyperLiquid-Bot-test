# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T04:07:30.114350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0225` n `12`; crypto_alt avg `-0.1198` n `230`; crypto_major avg `-0.1256` n `8`; equity avg `-0.0431` n `107`; fx avg `0.02` n `6`; index avg `-0.0156` n `25`; metal avg `-0.0024` n `20`; unknown avg `-0.0167` n `781`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `-0.1684` n `230`; crypto_major avg `-0.1002` n `8`; equity avg `0.151` n `107`; fx avg `0.0284` n `6`; index avg `-0.0049` n `25`; metal avg `0.0081` n `20`; unknown avg `0.0271` n `781`
- 4h: commodity avg `0.1163` n `12`; crypto_alt avg `0.0054` n `230`; crypto_major avg `0.1606` n `8`; equity avg `-0.3573` n `107`; fx avg `0.0109` n `6`; index avg `-0.1291` n `25`; metal avg `0.103` n `20`; unknown avg `-0.365` n `780`
- 24h: commodity avg `0.325` n `12`; crypto_alt avg `1.1119` n `230`; crypto_major avg `1.0418` n `8`; equity avg `1.594` n `107`; fx avg `0.0656` n `6`; index avg `0.0992` n `25`; metal avg `-0.0235` n `20`; unknown avg `0.2161` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
