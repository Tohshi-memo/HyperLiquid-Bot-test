# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T19:52:27.272556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `0.0755` n `235`; crypto_major avg `-0.0381` n `8`; equity avg `0.0037` n `150`; fx avg `0.0008` n `6`; index avg `-0.0013` n `26`; metal avg `0.0057` n `20`; unknown avg `5.0669` n `1134`
- 1h: commodity avg `0.031` n `13`; crypto_alt avg `0.3882` n `235`; crypto_major avg `0.1133` n `8`; equity avg `0.0492` n `150`; fx avg `-0.0042` n `6`; index avg `0.0085` n `26`; metal avg `0.0149` n `20`; unknown avg `1.5078` n `1130`
- 4h: commodity avg `0.0258` n `13`; crypto_alt avg `0.4865` n `235`; crypto_major avg `0.1068` n `8`; equity avg `0.1271` n `150`; fx avg `0.0032` n `6`; index avg `0.0261` n `26`; metal avg `0.0447` n `20`; unknown avg `0.0961` n `1092`
- 24h: commodity avg `0.2968` n `13`; crypto_alt avg `2.0372` n `235`; crypto_major avg `0.6378` n `8`; equity avg `0.2804` n `150`; fx avg `0.0213` n `6`; index avg `0.0452` n `26`; metal avg `0.0826` n `20`; unknown avg `0.8639` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
