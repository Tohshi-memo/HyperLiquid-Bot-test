# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T07:22:44.927217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0686` n `230`; crypto_major avg `-0.0641` n `8`; equity avg `-0.0338` n `102`; fx avg `-0.0004` n `6`; index avg `0.0001` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.0028` n `781`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0874` n `230`; crypto_major avg `-0.0867` n `8`; equity avg `-0.107` n `102`; fx avg `-0.0009` n `6`; index avg `-0.01` n `25`; metal avg `0.0135` n `20`; unknown avg `-0.0439` n `781`
- 4h: commodity avg `-0.1072` n `12`; crypto_alt avg `-0.0102` n `230`; crypto_major avg `-0.0889` n `8`; equity avg `-0.0341` n `102`; fx avg `-0.0086` n `6`; index avg `-0.0183` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.0739` n `765`
- 24h: commodity avg `0.7999` n `12`; crypto_alt avg `0.4411` n `230`; crypto_major avg `-1.2489` n `8`; equity avg `-2.2006` n `102`; fx avg `-0.0501` n `6`; index avg `-0.285` n `25`; metal avg `-0.1517` n `20`; unknown avg `4.8532` n `763`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
