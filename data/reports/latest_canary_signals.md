# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T23:07:28.568206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `12`; crypto_alt avg `0.0586` n `234`; crypto_major avg `0.0281` n `8`; equity avg `0.0297` n `140`; fx avg `0.0075` n `6`; index avg `0.0058` n `26`; metal avg `0.0109` n `20`; unknown avg `0.1014` n `940`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `-0.0788` n `234`; crypto_major avg `-0.1575` n `8`; equity avg `-0.0673` n `140`; fx avg `0.0061` n `6`; index avg `-0.0142` n `26`; metal avg `0.0173` n `20`; unknown avg `-0.0144` n `940`
- 4h: commodity avg `0.0539` n `12`; crypto_alt avg `0.5978` n `234`; crypto_major avg `0.2706` n `8`; equity avg `0.428` n `140`; fx avg `0.0471` n `6`; index avg `0.0617` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.4348` n `872`
- 24h: commodity avg `-0.0654` n `12`; crypto_alt avg `6.7441` n `234`; crypto_major avg `6.708` n `8`; equity avg `1.3355` n `140`; fx avg `0.2421` n `6`; index avg `0.051` n `26`; metal avg `0.3668` n `20`; unknown avg `4.0905` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
