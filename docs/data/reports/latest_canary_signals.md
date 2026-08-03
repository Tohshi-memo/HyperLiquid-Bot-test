# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T20:22:35.119440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `0.1738` n `230`; crypto_major avg `0.1982` n `8`; equity avg `0.1048` n `103`; fx avg `0.0057` n `6`; index avg `0.0246` n `25`; metal avg `0.015` n `20`; unknown avg `0.5992` n `784`
- 1h: commodity avg `-0.0676` n `12`; crypto_alt avg `-0.0086` n `230`; crypto_major avg `0.1522` n `8`; equity avg `0.1381` n `103`; fx avg `0.0186` n `6`; index avg `0.0398` n `25`; metal avg `0.0158` n `20`; unknown avg `-0.0926` n `784`
- 4h: commodity avg `0.0583` n `12`; crypto_alt avg `0.2724` n `230`; crypto_major avg `0.033` n `8`; equity avg `0.6814` n `103`; fx avg `-0.0016` n `6`; index avg `0.1334` n `25`; metal avg `0.1833` n `20`; unknown avg `0.127` n `784`
- 24h: commodity avg `-0.1479` n `12`; crypto_alt avg `0.5074` n `230`; crypto_major avg `0.6799` n `8`; equity avg `2.0269` n `103`; fx avg `-0.2548` n `6`; index avg `0.0868` n `25`; metal avg `-0.3941` n `20`; unknown avg `0.0279` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
