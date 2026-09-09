# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T17:37:27.536059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.08` n `12`; crypto_alt avg `-0.0615` n `233`; crypto_major avg `0.1176` n `8`; equity avg `-0.0503` n `134`; fx avg `0.0118` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0554` n `20`; unknown avg `-0.0172` n `797`
- 1h: commodity avg `-0.0665` n `12`; crypto_alt avg `0.2438` n `233`; crypto_major avg `0.178` n `8`; equity avg `-0.019` n `134`; fx avg `0.0399` n `6`; index avg `0.0179` n `26`; metal avg `0.113` n `20`; unknown avg `-0.1952` n `795`
- 4h: commodity avg `-0.0967` n `12`; crypto_alt avg `-0.4513` n `233`; crypto_major avg `-0.5086` n `8`; equity avg `-0.3913` n `134`; fx avg `0.0453` n `6`; index avg `-0.0716` n `26`; metal avg `0.0089` n `20`; unknown avg `4.6201` n `767`
- 24h: commodity avg `0.4317` n `12`; crypto_alt avg `-0.7669` n `233`; crypto_major avg `-0.0748` n `8`; equity avg `-0.7477` n `134`; fx avg `-0.057` n `6`; index avg `-0.2406` n `26`; metal avg `0.4102` n `20`; unknown avg `5.4427` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
