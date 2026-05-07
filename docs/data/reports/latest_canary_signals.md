# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T03:22:15.964008+00:00`
- Correlation status: `ready`
- Asset price records: `513`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.178` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.007` n `12`; crypto_alt avg `-0.1851` n `228`; crypto_major avg `-0.1832` n `8`; equity avg `-0.0595` n `65`; fx avg `0.0144` n `4`; index avg `0.0068` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.0935` n `358`
- 1h: commodity avg `0.0637` n `12`; crypto_alt avg `0.0954` n `228`; crypto_major avg `-0.1582` n `8`; equity avg `0.0445` n `65`; fx avg `0.0401` n `4`; index avg `0.0531` n `23`; metal avg `0.1038` n `18`; unknown avg `-0.1444` n `358`
- 4h: commodity avg `-0.0988` n `12`; crypto_alt avg `-0.8766` n `228`; crypto_major avg `-1.0427` n `8`; equity avg `-0.1847` n `65`; fx avg `0.0964` n `4`; index avg `0.1353` n `23`; metal avg `0.31` n `18`; unknown avg `-0.5218` n `356`
- 24h: commodity avg `-1.7966` n `7`; crypto_alt avg `0.1402` n `223`; crypto_major avg `-1.3032` n `7`; equity avg `1.3698` n `47`; fx avg `-0.2366` n `4`; index avg `1.3048` n `6`; metal avg `1.6561` n `7`; unknown avg `1.7074` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1296`, n `509`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `509`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `509`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `509`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0751`, n `505`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0688`, n `505`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0687`, n `505`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `509`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0664`, n `505`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0655`, n `505`, weak_sample_signal
