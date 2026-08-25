# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T14:07:34.381060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0479` n `12`; crypto_alt avg `0.8402` n `231`; crypto_major avg `0.9298` n `8`; equity avg `-0.1372` n `122`; fx avg `0.0045` n `6`; index avg `-0.0614` n `25`; metal avg `0.1059` n `20`; unknown avg `0.3488` n `795`
- 1h: commodity avg `0.0763` n `12`; crypto_alt avg `-0.5626` n `231`; crypto_major avg `-0.4109` n `8`; equity avg `0.1594` n `122`; fx avg `0.024` n `6`; index avg `-0.0443` n `25`; metal avg `0.0489` n `20`; unknown avg `-0.1551` n `795`
- 4h: commodity avg `-0.1211` n `12`; crypto_alt avg `-0.9351` n `231`; crypto_major avg `-0.9092` n `8`; equity avg `-0.1871` n `122`; fx avg `0.0198` n `6`; index avg `-0.0945` n `25`; metal avg `-0.0593` n `20`; unknown avg `-0.1513` n `795`
- 24h: commodity avg `-0.8337` n `12`; crypto_alt avg `-0.8885` n `231`; crypto_major avg `-0.3757` n `8`; equity avg `2.218` n `122`; fx avg `0.051` n `6`; index avg `0.3004` n `25`; metal avg `-0.449` n `20`; unknown avg `-0.916` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
