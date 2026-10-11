# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T20:07:29.154948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `13`; crypto_alt avg `0.0357` n `235`; crypto_major avg `-0.0315` n `8`; equity avg `-0.0068` n `150`; fx avg `0.0044` n `6`; index avg `-0.0014` n `26`; metal avg `0.0035` n `20`; unknown avg `0.029` n `1118`
- 1h: commodity avg `0.0368` n `13`; crypto_alt avg `0.2717` n `235`; crypto_major avg `0.0141` n `8`; equity avg `0.0257` n `150`; fx avg `0.0078` n `6`; index avg `0.0065` n `26`; metal avg `0.0175` n `20`; unknown avg `0.0292` n `1118`
- 4h: commodity avg `0.0693` n `13`; crypto_alt avg `0.0974` n `235`; crypto_major avg `-0.3299` n `8`; equity avg `0.0518` n `150`; fx avg `0.0124` n `6`; index avg `0.0183` n `26`; metal avg `0.0458` n `20`; unknown avg `0.1376` n `1100`
- 24h: commodity avg `0.3186` n `13`; crypto_alt avg `1.9618` n `235`; crypto_major avg `0.5811` n `8`; equity avg `0.2721` n `150`; fx avg `0.0257` n `6`; index avg `0.0372` n `26`; metal avg `0.0879` n `20`; unknown avg `0.8278` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
