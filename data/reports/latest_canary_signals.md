# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T19:22:34.519569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5069` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.377` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.008` n `13`; crypto_alt avg `-0.095` n `239`; crypto_major avg `-0.0163` n `8`; equity avg `-0.3196` n `157`; fx avg `0.0074` n `6`; index avg `-0.0508` n `27`; metal avg `-0.0295` n `20`; unknown avg `28.3858` n `1264`
- 1h: commodity avg `0.0723` n `13`; crypto_alt avg `-0.4456` n `239`; crypto_major avg `-0.2755` n `8`; equity avg `-1.2309` n `157`; fx avg `0.0056` n `6`; index avg `-0.1367` n `27`; metal avg `-0.1297` n `20`; unknown avg `15.1085` n `1214`
- 4h: commodity avg `-0.3676` n `13`; crypto_alt avg `-1.9097` n `239`; crypto_major avg `-1.6606` n `8`; equity avg `-2.7747` n `157`; fx avg `-0.0134` n `6`; index avg `-0.2836` n `27`; metal avg `-0.1537` n `20`; unknown avg `7.5328` n `1182`
- 24h: commodity avg `-1.3267` n `13`; crypto_alt avg `-2.6637` n `238`; crypto_major avg `-1.5271` n `8`; equity avg `-2.5612` n `157`; fx avg `0.2579` n `6`; index avg `0.0577` n `27`; metal avg `0.2424` n `20`; unknown avg `4.3728` n `1012`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
