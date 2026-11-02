# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T23:22:28.349217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `13`; crypto_alt avg `-0.0391` n `239`; crypto_major avg `-0.0719` n `8`; equity avg `0.2932` n `157`; fx avg `0.0081` n `6`; index avg `0.0703` n `27`; metal avg `-0.0015` n `20`; unknown avg `158.3576` n `1262`
- 1h: commodity avg `-0.0329` n `13`; crypto_alt avg `-0.1327` n `239`; crypto_major avg `-0.1408` n `8`; equity avg `0.3034` n `157`; fx avg `-0.0143` n `6`; index avg `0.0612` n `27`; metal avg `-0.0094` n `20`; unknown avg `0.2705` n `1250`
- 4h: commodity avg `-0.0597` n `13`; crypto_alt avg `0.2945` n `239`; crypto_major avg `0.3084` n `8`; equity avg `0.1095` n `157`; fx avg `-0.0196` n `6`; index avg `-0.0075` n `27`; metal avg `-0.0225` n `20`; unknown avg `13.6198` n `1144`
- 24h: commodity avg `-1.3889` n `13`; crypto_alt avg `-2.8117` n `238`; crypto_major avg `-1.4781` n `8`; equity avg `-2.5766` n `157`; fx avg `0.2387` n `6`; index avg `0.0472` n `27`; metal avg `0.1328` n `20`; unknown avg `13.0935` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
