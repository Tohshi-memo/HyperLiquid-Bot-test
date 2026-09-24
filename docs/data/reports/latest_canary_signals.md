# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T03:52:27.387988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `-0.1532` n `234`; crypto_major avg `-0.1436` n `8`; equity avg `-0.0293` n `141`; fx avg `-0.0103` n `6`; index avg `-0.0082` n `26`; metal avg `0.0061` n `20`; unknown avg `3.3924` n `945`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.6072` n `234`; crypto_major avg `-0.6191` n `8`; equity avg `-0.2335` n `141`; fx avg `0.0075` n `6`; index avg `-0.0317` n `26`; metal avg `-0.0181` n `20`; unknown avg `1.9226` n `943`
- 4h: commodity avg `-0.0644` n `12`; crypto_alt avg `0.4082` n `234`; crypto_major avg `-0.4528` n `8`; equity avg `-0.3856` n `141`; fx avg `0.0427` n `6`; index avg `-0.0455` n `26`; metal avg `-0.0523` n `20`; unknown avg `1.659` n `937`
- 24h: commodity avg `0.5108` n `12`; crypto_alt avg `-5.1627` n `234`; crypto_major avg `-4.7455` n `8`; equity avg `-1.7657` n `140`; fx avg `0.0826` n `6`; index avg `-0.3459` n `26`; metal avg `-0.665` n `20`; unknown avg `585.6063` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
