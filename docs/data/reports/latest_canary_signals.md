# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T03:37:30.147770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.3436` n `239`; crypto_major avg `-0.2956` n `8`; equity avg `-0.267` n `157`; fx avg `0.0118` n `6`; index avg `-0.0581` n `27`; metal avg `-0.0547` n `20`; unknown avg `1.7183` n `1264`
- 1h: commodity avg `0.0163` n `13`; crypto_alt avg `-0.7189` n `239`; crypto_major avg `-0.6343` n `8`; equity avg `-0.5126` n `157`; fx avg `0.0021` n `6`; index avg `-0.0388` n `27`; metal avg `-0.1435` n `20`; unknown avg `0.9457` n `1258`
- 4h: commodity avg `0.1428` n `13`; crypto_alt avg `-0.9581` n `239`; crypto_major avg `-0.4504` n `8`; equity avg `-0.3956` n `157`; fx avg `-0.0695` n `6`; index avg `-0.0525` n `27`; metal avg `-0.2407` n `20`; unknown avg `0.3294` n `1252`
- 24h: commodity avg `-0.9121` n `13`; crypto_alt avg `-4.1361` n `238`; crypto_major avg `-2.9182` n `8`; equity avg `-4.1852` n `157`; fx avg `-0.0407` n `6`; index avg `-0.2703` n `27`; metal avg `-0.1033` n `20`; unknown avg `12.5846` n `1014`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
