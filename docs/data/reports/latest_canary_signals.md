# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T05:37:31.452004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0441` n `12`; crypto_alt avg `-0.7533` n `234`; crypto_major avg `-0.6294` n `8`; equity avg `-0.3017` n `141`; fx avg `-0.007` n `6`; index avg `-0.0628` n `26`; metal avg `-0.0914` n `20`; unknown avg `2.0754` n `963`
- 1h: commodity avg `0.032` n `12`; crypto_alt avg `-0.5285` n `234`; crypto_major avg `-0.4101` n `8`; equity avg `-0.2822` n `141`; fx avg `-0.0244` n `6`; index avg `-0.0681` n `26`; metal avg `-0.0563` n `20`; unknown avg `0.4871` n `961`
- 4h: commodity avg `0.0811` n `12`; crypto_alt avg `0.1537` n `234`; crypto_major avg `0.2198` n `8`; equity avg `-0.5142` n `141`; fx avg `-0.0606` n `6`; index avg `-0.1414` n `26`; metal avg `-0.1079` n `20`; unknown avg `0.6152` n `955`
- 24h: commodity avg `0.0798` n `12`; crypto_alt avg `-1.8039` n `234`; crypto_major avg `-0.5107` n `8`; equity avg `-2.2864` n `141`; fx avg `-0.1133` n `6`; index avg `-0.3024` n `26`; metal avg `-0.4891` n `20`; unknown avg `10.4432` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
