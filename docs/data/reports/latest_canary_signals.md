# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T18:22:32.025352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `0.0806` n `234`; crypto_major avg `0.0766` n `8`; equity avg `-0.0393` n `141`; fx avg `-0.0023` n `6`; index avg `0.0045` n `26`; metal avg `-0.0023` n `20`; unknown avg `-0.0946` n `963`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.3365` n `234`; crypto_major avg `-0.0923` n `8`; equity avg `-0.0116` n `141`; fx avg `0.0067` n `6`; index avg `0.0064` n `26`; metal avg `-0.0203` n `20`; unknown avg `0.2719` n `961`
- 4h: commodity avg `-0.3124` n `12`; crypto_alt avg `0.5076` n `234`; crypto_major avg `0.4576` n `8`; equity avg `-0.0105` n `141`; fx avg `0.0214` n `6`; index avg `0.0064` n `26`; metal avg `0.0054` n `20`; unknown avg `16.6325` n `944`
- 24h: commodity avg `-0.5052` n `12`; crypto_alt avg `-2.9337` n `234`; crypto_major avg `-1.478` n `8`; equity avg `-2.9783` n `141`; fx avg `0.042` n `6`; index avg `-0.2623` n `26`; metal avg `-0.9574` n `20`; unknown avg `23.0311` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
