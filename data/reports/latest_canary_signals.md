# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T02:07:34.992894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0916` n `12`; crypto_alt avg `0.0765` n `230`; crypto_major avg `0.1952` n `8`; equity avg `0.0516` n `108`; fx avg `0.0012` n `6`; index avg `0.0107` n `25`; metal avg `0.0244` n `20`; unknown avg `0.226` n `781`
- 1h: commodity avg `-0.0863` n `12`; crypto_alt avg `0.4934` n `230`; crypto_major avg `0.6431` n `8`; equity avg `0.4109` n `108`; fx avg `-0.0076` n `6`; index avg `0.0357` n `25`; metal avg `0.1246` n `20`; unknown avg `0.6822` n `781`
- 4h: commodity avg `0.1105` n `12`; crypto_alt avg `0.2721` n `230`; crypto_major avg `0.3046` n `8`; equity avg `0.7147` n `108`; fx avg `-0.0734` n `6`; index avg `0.0947` n `25`; metal avg `0.0919` n `20`; unknown avg `-0.1779` n `781`
- 24h: commodity avg `-1.315` n `12`; crypto_alt avg `0.1989` n `230`; crypto_major avg `0.7352` n `8`; equity avg `3.9165` n `107`; fx avg `0.0801` n `6`; index avg `0.8118` n `25`; metal avg `0.8712` n `20`; unknown avg `0.3738` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
