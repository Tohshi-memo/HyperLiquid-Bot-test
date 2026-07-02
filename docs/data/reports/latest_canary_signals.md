# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T02:52:29.909479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0352` n `228`; crypto_major avg `-0.0436` n `8`; equity avg `-0.0428` n `88`; fx avg `-0.0011` n `6`; index avg `-0.0168` n `25`; metal avg `0.0229` n `20`; unknown avg `4.6996` n `763`
- 1h: commodity avg `0.0172` n `12`; crypto_alt avg `0.1566` n `228`; crypto_major avg `0.209` n `8`; equity avg `-0.1145` n `88`; fx avg `-0.0217` n `6`; index avg `-0.0511` n `25`; metal avg `0.0766` n `20`; unknown avg `0.1095` n `763`
- 4h: commodity avg `-0.1005` n `12`; crypto_alt avg `0.1319` n `228`; crypto_major avg `-0.0668` n `8`; equity avg `-0.0972` n `88`; fx avg `-0.0015` n `6`; index avg `0.0319` n `25`; metal avg `0.2976` n `20`; unknown avg `21.4872` n `761`
- 24h: commodity avg `-0.6195` n `12`; crypto_alt avg `2.011` n `228`; crypto_major avg `1.0854` n `8`; equity avg `-1.0162` n `88`; fx avg `-0.029` n `6`; index avg `-0.2715` n `25`; metal avg `1.0499` n `20`; unknown avg `25.0832` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
