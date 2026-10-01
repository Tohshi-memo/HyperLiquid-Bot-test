# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T06:37:34.595681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0752` n `13`; crypto_alt avg `-0.0547` n `234`; crypto_major avg `-0.0842` n `8`; equity avg `-0.07` n `142`; fx avg `0.0015` n `6`; index avg `-0.0237` n `26`; metal avg `-0.0636` n `20`; unknown avg `0.2145` n `974`
- 1h: commodity avg `0.1988` n `13`; crypto_alt avg `0.0387` n `234`; crypto_major avg `-0.0214` n `8`; equity avg `0.0906` n `142`; fx avg `-0.0012` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0958` n `20`; unknown avg `-0.0252` n `946`
- 4h: commodity avg `-0.2852` n `13`; crypto_alt avg `0.9518` n `234`; crypto_major avg `0.7066` n `8`; equity avg `0.8665` n `142`; fx avg `-0.0284` n `6`; index avg `0.1627` n `26`; metal avg `0.1686` n `20`; unknown avg `0.4369` n `940`
- 24h: commodity avg `-0.2237` n `13`; crypto_alt avg `1.9481` n `234`; crypto_major avg `1.7418` n `8`; equity avg `1.2332` n `142`; fx avg `0.137` n `6`; index avg `0.2962` n `26`; metal avg `-0.0269` n `20`; unknown avg `777.3911` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
