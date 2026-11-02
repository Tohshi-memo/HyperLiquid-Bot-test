# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T19:52:32.357519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1768` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0037` n `13`; crypto_alt avg `-0.0303` n `239`; crypto_major avg `0.1856` n `8`; equity avg `0.0214` n `157`; fx avg `-0.0043` n `6`; index avg `0.0098` n `27`; metal avg `-0.0012` n `20`; unknown avg `3.7702` n `1264`
- 1h: commodity avg `0.0523` n `13`; crypto_alt avg `-0.448` n `239`; crypto_major avg `-0.1568` n `8`; equity avg `-0.8681` n `157`; fx avg `0.0079` n `6`; index avg `-0.1133` n `27`; metal avg `-0.0714` n `20`; unknown avg `1.9028` n `1232`
- 4h: commodity avg `-0.3745` n `13`; crypto_alt avg `-2.0379` n `239`; crypto_major avg `-1.4472` n `8`; equity avg `-2.7267` n `157`; fx avg `-0.0103` n `6`; index avg `-0.2704` n `27`; metal avg `-0.2082` n `20`; unknown avg `7.7603` n `1184`
- 24h: commodity avg `-1.3285` n `13`; crypto_alt avg `-3.0494` n `238`; crypto_major avg `-1.5374` n `8`; equity avg `-2.7507` n `157`; fx avg `0.2668` n `6`; index avg `0.0273` n `27`; metal avg `0.1973` n `20`; unknown avg `3.795` n `1012`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
