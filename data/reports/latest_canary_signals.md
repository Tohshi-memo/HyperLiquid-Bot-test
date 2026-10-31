# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T16:22:28.003828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0459` n `13`; crypto_alt avg `-0.1137` n `238`; crypto_major avg `-0.0366` n `8`; equity avg `0.0089` n `156`; fx avg `-0.0003` n `6`; index avg `0.0097` n `27`; metal avg `0.0076` n `20`; unknown avg `2.6418` n `1262`
- 1h: commodity avg `-0.0383` n `13`; crypto_alt avg `0.2918` n `238`; crypto_major avg `0.1681` n `8`; equity avg `0.015` n `156`; fx avg `-0.0172` n `6`; index avg `-0.0019` n `27`; metal avg `0.0068` n `20`; unknown avg `1.9502` n `1236`
- 4h: commodity avg `-0.1444` n `13`; crypto_alt avg `0.8633` n `238`; crypto_major avg `0.0519` n `8`; equity avg `0.069` n `156`; fx avg `-0.0161` n `6`; index avg `-0.0061` n `27`; metal avg `0.0292` n `20`; unknown avg `3.9778` n `1236`
- 24h: commodity avg `-0.4472` n `13`; crypto_alt avg `1.2717` n `238`; crypto_major avg `-0.0722` n `8`; equity avg `0.3212` n `156`; fx avg `-0.0283` n `6`; index avg `-0.0518` n `27`; metal avg `0.0047` n `20`; unknown avg `1.8235` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
