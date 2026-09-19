# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T23:22:26.275803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0351` n `12`; crypto_alt avg `-0.1764` n `234`; crypto_major avg `-0.0397` n `8`; equity avg `-0.0257` n `140`; fx avg `-0.0218` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.2075` n `943`
- 1h: commodity avg `0.033` n `12`; crypto_alt avg `0.6804` n `234`; crypto_major avg `0.5483` n `8`; equity avg `-0.0185` n `140`; fx avg `-0.02` n `6`; index avg `-0.007` n `26`; metal avg `-0.0095` n `20`; unknown avg `6.1195` n `941`
- 4h: commodity avg `0.0501` n `12`; crypto_alt avg `-0.3119` n `234`; crypto_major avg `-0.6381` n `8`; equity avg `0.0316` n `140`; fx avg `-0.0478` n `6`; index avg `0.0038` n `26`; metal avg `-0.0119` n `20`; unknown avg `4.4348` n `911`
- 24h: commodity avg `0.1067` n `12`; crypto_alt avg `0.8098` n `234`; crypto_major avg `-0.26` n `8`; equity avg `-0.0266` n `140`; fx avg `-0.0969` n `6`; index avg `0.0178` n `26`; metal avg `-0.0304` n `20`; unknown avg `2.0132` n `838`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
