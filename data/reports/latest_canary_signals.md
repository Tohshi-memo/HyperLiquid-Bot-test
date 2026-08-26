# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T23:22:27.461098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.2171` n `231`; crypto_major avg `0.3568` n `8`; equity avg `0.0852` n `124`; fx avg `0.0135` n `6`; index avg `-0.0019` n `25`; metal avg `0.0479` n `20`; unknown avg `-0.0307` n `795`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `0.0162` n `231`; crypto_major avg `-0.38` n `8`; equity avg `0.0455` n `124`; fx avg `0.0067` n `6`; index avg `0.0002` n `25`; metal avg `0.0465` n `20`; unknown avg `0.2143` n `795`
- 4h: commodity avg `-0.0175` n `12`; crypto_alt avg `1.8405` n `231`; crypto_major avg `1.5476` n `8`; equity avg `1.6733` n `124`; fx avg `-0.0013` n `6`; index avg `0.2717` n `25`; metal avg `0.1921` n `20`; unknown avg `0.5281` n `795`
- 24h: commodity avg `0.3133` n `12`; crypto_alt avg `1.37` n `231`; crypto_major avg `1.0429` n `8`; equity avg `1.5314` n `124`; fx avg `-0.0618` n `6`; index avg `0.3088` n `25`; metal avg `-0.2223` n `20`; unknown avg `1.0416` n `777`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
