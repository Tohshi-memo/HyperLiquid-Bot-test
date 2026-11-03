# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T14:37:31.710539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0853` n `13`; crypto_alt avg `0.1711` n `239`; crypto_major avg `0.2238` n `8`; equity avg `0.4591` n `157`; fx avg `0.0168` n `6`; index avg `0.038` n `27`; metal avg `-0.0255` n `20`; unknown avg `1.0918` n `1264`
- 1h: commodity avg `0.2863` n `13`; crypto_alt avg `-0.2732` n `239`; crypto_major avg `0.0255` n `8`; equity avg `0.0232` n `157`; fx avg `0.0312` n `6`; index avg `-0.0189` n `27`; metal avg `-0.0913` n `20`; unknown avg `295.6728` n `1256`
- 4h: commodity avg `-0.5213` n `13`; crypto_alt avg `1.1222` n `239`; crypto_major avg `1.0162` n `8`; equity avg `1.0687` n `157`; fx avg `0.0118` n `6`; index avg `0.1251` n `27`; metal avg `0.3589` n `20`; unknown avg `6.3055` n `1222`
- 24h: commodity avg `-0.458` n `13`; crypto_alt avg `-0.6766` n `239`; crypto_major avg `-0.0293` n `8`; equity avg `-0.7504` n `157`; fx avg `0.0241` n `6`; index avg `-0.0254` n `27`; metal avg `-0.3908` n `20`; unknown avg `-0.1791` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
