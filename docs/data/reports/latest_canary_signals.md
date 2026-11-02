# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T19:07:41.172942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5303` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4469` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0172` n `13`; crypto_alt avg `-0.0708` n `239`; crypto_major avg `-0.0892` n `8`; equity avg `-0.3432` n `157`; fx avg `0.0052` n `6`; index avg `-0.0271` n `27`; metal avg `0.0076` n `20`; unknown avg `0.5764` n `1232`
- 1h: commodity avg `0.1307` n `13`; crypto_alt avg `-0.5819` n `239`; crypto_major avg `-0.5198` n `8`; equity avg `-1.1051` n `157`; fx avg `-0.0054` n `6`; index avg `-0.105` n `27`; metal avg `-0.1059` n `20`; unknown avg `1.2115` n `1214`
- 4h: commodity avg `-0.3806` n `13`; crypto_alt avg `-1.745` n `239`; crypto_major avg `-1.6057` n `8`; equity avg `-2.0848` n `157`; fx avg `-0.0081` n `6`; index avg `-0.1588` n `27`; metal avg `-0.0754` n `20`; unknown avg `17.1453` n `1182`
- 24h: commodity avg `-1.3292` n `13`; crypto_alt avg `-2.8598` n `238`; crypto_major avg `-1.6848` n `8`; equity avg `-2.3066` n `157`; fx avg `0.2506` n `6`; index avg `0.0917` n `27`; metal avg `0.2523` n `20`; unknown avg `4.3218` n `1006`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
